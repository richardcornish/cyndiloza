function drawMap(address, latitude, longitude, maptype) {
    if (GBrowserIsCompatible()) {

        var map = new GMap2(document.getElementById("map"));
        map.addControl(new GSmallZoomControl3D());        
        map.addControl(new GMenuMapTypeControl());
        map.addControl(new GScaleControl());
        map.addMapType(G_PHYSICAL_MAP);
        map.addMapType(G_SATELLITE_3D_MAP);
        map.addMapType(G_MAPMAKER_NORMAL_MAP); 
        map.addMapType(G_MAPMAKER_HYBRID_MAP);
        // GoogleMaps requires a centered rendering point before moving it to the desired location (I think)
        // I choose the center of the United States, the same one on http://maps.google.com
        var center = new GLatLng(37.0625, -95.677068);
        var zoom = 15;
        var type = maptype;
        map.setCenter(center, zoom, type);
        
        // Address GeoCoder
        var geocoder = new GClientGeocoder();
        var address = address;
        geocoder.getLatLng(address, function(point) {
            if (point) {
               // I get weird results if I try to pass the GeoCoded latitude and longitude point,
               // so I'm just going to re-assign the point as the latitude and longitude instead
               // of the human-friendly address. Sorry, the world ain't a perfect place!
               var point = new GLatLng(latitude, longitude);
               map.setCenter(point, 15);
               markerOptions = { clickable: false };
               var marker = new GMarker(point, markerOptions);
               map.addOverlay(marker);

               // Google StreetView panorama
               var street = new GStreetviewClient();
               street.getNearestPanoramaLatLng(point, function(point2) {
                   if (point2) {
                     var pano = document.getElementById("pano");
                     var width = "500px";
                     var height = "300px";
                     pano.style.width = width;
                     pano.style.height = height;
                     //var pov = { yaw: 0, pitch: 0, zoom: 0 };
                     var options = { latlng: point2 };
                     var view = new GStreetviewPanorama(pano, options);
                     // GEvent.addListener(view, "error", errorFunction);
                     } else {
                         document.getElementById("pano").style.display = "none";
                     }
                });

               // Currently not using...
               // Error handler for Google StreetView
               function errorFunction(errorCode) {
                   if (errorCode == 600) {
                     // No panorama location exists
                     pano.style.display = "none";
                     return;
                   } if (errorCode == 603) {
                     // Adobe Flash not installed
                     pano.style.height = "auto";
                     var link = document.createElement("a");
                     link.setAttribute("href", "http://www.adobe.com/go/EN_US-H-GET-FLASH");
                     var linkText = document.createTextNode("Adobe Flash Player");
                     link.appendChild(linkText);
                     var text1 = document.createTextNode("Please download the ");
                     var text2 = document.createTextNode(".");
                     var paragraph = document.createElement("p");
                     paragraph.appendChild(text1);
                     paragraph.appendChild(link);
                     paragraph.appendChild(text2);
                     pano.appendChild(paragraph);
                     return;
                   }
               }
               
            } else {
                // Need better error-handling code here
            }
        });
        
    }
}

function drawPublicationsMap(url, data) {
    if (GBrowserIsCompatible()) {
        
        // Create map and set up defaults
        var map = new GMap2(document.getElementById("map-places"));
        var center = new GLatLng(37.0625, -95.677068);
        map.setCenter(center, 3, G_PHYSICAL_MAP);
        map.addControl(new GLargeMapControl3D());
        map.addControl(new GMenuMapTypeControl());
        map.addControl(new GScaleControl());
        map.addMapType(G_PHYSICAL_MAP);
        map.addMapType(G_SATELLITE_3D_MAP);
        // var overview = new GOverviewMapControl(new GSize(150, 100));
        // overview.hide(true);
        // map.addControl(overview);
        map.enableContinuousZoom();
        map.enableScrollWheelZoom();
        
        // Heat map
        var myHM = new GEOHeatmap();
        myHM.Init(830, 400); // width, height
        myHM.SetData(data);
        myHM.SetBoost(.5); // optional
        myHM.SetDecay(1); // optional
        var preUrl = myHM.GetURL();
        var heatmapOverlay = new HMGoogleOverlay(preUrl);
        map.addOverlay(heatmapOverlay);

        // Create marker function
        function createMarker(point, html, icon, width, height) {
            var customIcon = new GIcon(G_DEFAULT_ICON);
            customIcon.image = icon;
            // customIcon.shadow = "http://maps.google.com/mapfiles/ms/micons/pushpin_shadow.png";
            customIcon.iconSize = new GSize(width, height);
            // customIcon.shadowSize = new GSize(59, 32);
            // customIcon.iconAnchor = new GPoint(6, 20);
            // customIcon.infoWindowAnchor = new GPoint(5, 1);
            // customIcon.printImage = "http://www.google.com/mapfiles/markerie.gif";
            // customIcon.mozPrintImage = "http://www.google.com/mapfiles/markerff.gif";
            // customIcon.transparent = "http://www.google.com/mapfiles/markerTransparent.png";
            // customIcon.printShadow = "http://www.google.com/mapfiles/dithshadow.gif";
            // customIcon.imageMap = [0, 0, 12, 0, 12, 20, 0, 20];            
            markerOptions = { icon: customIcon, clickable: true };
            var marker = new GMarker(point, markerOptions);
            var options = { maxWidth: 200 };
            GEvent.addListener(marker, "click", function() {
                // map.panTo(point);
                marker.openInfoWindowHtml(html, options);
            });
            return marker;
        }

        // Load up the URL of the XML
        // var url = "http://www.cyndiloza.com/publications/all/xml/";
        GDownloadUrl(url, function(data, responseCode) {
            var batch = [];
            var bounds = new GLatLngBounds();
            var xml = GXml.parse(data);
            var markers = xml.documentElement.getElementsByTagName("marker");
            for (var i = 0; i < markers.length; i++) {
                var point = new GLatLng(parseFloat(markers[i].getAttribute("lat")),
                                        parseFloat(markers[i].getAttribute("lng")));
                var headline = markers[i].getAttribute("headline");
                var summary = markers[i].getAttribute("summary");
                var url = markers[i].getAttribute("url");
                var html = '<span class="info"><a href="' + url + '" class="headline">' + headline + '</a>' + summary + '</span>';
                var icon = markers[i].getAttribute("icon");
                var width = markers[i].getAttribute("width");
                var height = markers[i].getAttribute("height");
                var marker = createMarker(point, html, icon, width, height);
                batch.push(marker);
                bounds.extend(point);
            }
            new_zoom = map.getBoundsZoomLevel(bounds);
            new_center = bounds.getCenter();
            map.setZoom(new_zoom);
            map.setCenter(new_center);
            var mgr = new MarkerManager(map);
            mgr.addMarkers(batch, 4);
            mgr.refresh();
        });
        
        // Reset map
        var paragraphs = document.getElementsByTagName('p');
        for (var i = 0; i < paragraphs.length; i++) {
          if (paragraphs[i].className == 'note') {
            var paragraph = paragraphs[i];
            var bullet = document.createElement('span');
            var glyph = document.createTextNode('\u2022');
            bullet.className = 'bullet';
            bullet.appendChild(glyph);
            var reset = document.createElement('a');
            var text = document.createTextNode('Reset the map');
            reset.appendChild(text);
            paragraph.appendChild(bullet);
            paragraph.appendChild(reset);
          }
        }
        reset.onclick = function(){
          map.setZoom(new_zoom);
          map.setCenter(new_center);
        }
    }
}
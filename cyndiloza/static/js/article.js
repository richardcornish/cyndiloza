$(document).ready(function(){

  // Animated map
  $("#map-detail").append("<p class=\"button\"><button id=\"expand\">Expand</button></p>");
  $("button#expand").toggle(function(){
    $("div#map").animate({ height: "350px" }, "500");
    $("button#expand").text("Collapse");
  }, function(){
    $("div#map").animate({ height: "150px" }, "500");
    $("button#expand").text("Expand");
  });

  // Print article link
  $("span#print").text("Print article");
  $("span#print").wrapInner("<a href=\"#\"></a>");
  $("span#print").prepend("<span class=\"bullet\">&#8226;</span> ");
  $("span#print").click(function(){
    window.print();
  });

  // Text-size changer. Kind of long, but whaddaya gonna do?
  $("span#small").css({ fontWeight: "bold" });

  $("span#small").text("A").css({ fontSize: "100%", paddingRight: "5px" });
  $("span#small").wrapInner("<a href=\"#\"></a>");
  $("span#small").click(function(){
    $(this).css({ fontWeight: "bold" });
    $("span#medium, span#big").css({ fontWeight: "normal"});
    $("div#story").css({ fontSize: "100%"});
  });

  $("span#medium").text("A").css({ fontSize: "115%" });
  $("span#medium").wrapInner("<a href=\"#\"></a>");
  $("span#medium").click(function(){
    $(this).css({ fontWeight: "bold"});
    $("span#small, span#big").css({ fontWeight: "normal" });
    $("div#story").css({ fontSize: "115%"});
  });

  $("span#big").text("A").css({ fontSize: "130%", paddingLeft: "5px" });
  $("span#big").wrapInner("<a href=\"#\"></a>");
  $("span#big").click(function(){
    $(this).css({ fontWeight: "bold" });
    $("span#small, span#medium").css({ fontWeight: "normal" });
    $("div#story").css({ fontSize: "130%" });
  });

  // For print stylesheet
  $("p.url").append(" <span class=\"archive\">This article is archived at " + window.location.href + "</span>");

});
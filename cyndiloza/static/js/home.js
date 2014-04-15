// Google Charts JavaScript function
function drawChart(valueArray, chartLabels) {

  // Assign the maximum value of that array to maxValue. Thanks, John!
  // http://ejohn.org/blog/fast-javascript-maxmin/
  Array.max = function(array){
    return Math.max.apply(Math, array);
  };
  var maxValue = Array.max(valueArray);
 
  // Google Charts' Simple Encoding JavaScript function. Thanks, Google!
  // http://code.google.com/apis/chart/formats.html#encoding_data
  var simpleEncoding = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  function simpleEncode(valueArray, maxValue) {
  var chartData = ['s:'];
    for (var i = 0; i < valueArray.length; i++) {
      var currentValue = valueArray[i];
      if (!isNaN(currentValue) && currentValue >= 0) {
      chartData.push(simpleEncoding.charAt(Math.round((simpleEncoding.length-1) * currentValue / maxValue)));
      }
        else {
        chartData.push('_');
        }
    }
  return chartData.join('');
  }
  
  // Pass in array and maximum value to simpleEncode function, assigning result to the chartData variable
  var chartData = simpleEncode(valueArray, maxValue);
  
  // Assign chartPie variable "p" for 2-D pie chart or "p3" for 3-D pie chart
  var chartPie = "p";
  
  // Assign chartColor variable a hex without the hash mark
  var chartColor = "cc0000"
  
  // Assign width and height variables the width and height of the chart in pixels; customize as necessary
  var width = 395;
  var height = 125;
  var chartSize = width + "x" + height;

  // Attach all of your crap to the chart image source attribute
  var original = $("img#chart").attr("src");
  $("img#chart").attr("src", original + "&cht=" + chartPie + "&chco=" + chartColor + "&chs=" + chartSize + "&chd=" + chartData + "&chl=" + chartLabels);
  
}

// jQuery slidey bar chart
$(document).ready(function(){
  
  // Promo slide
  // $("#promo-wrap").css({ marginTop: "-28px" });
  // $("#promo").prepend('<img src="http://media.cyndiloza.com/static/img/facebook.gif" width="101" height="37" alt="Facebook logo" />');
  // $("#promo img").css({ top: "-9px" }).animate({ opacity: 1 }, 1000);
  // $("#promo img").animate({ top: "28px" }, 1000);
  // $("#promo img").toggle(function(){
  //   $("#promo-wrap").stop().animate({ marginTop: "0px", }, 500);
  // }, function(){
  //   $("#promo-wrap").stop().animate({ marginTop: "-28px", }, 500);
  // });

  // Slidey charts link replacement
  $("#words li a").mouseover(function(){
    var link = $(this).attr("href");
    var title = $(this).attr("title");
    $("span#headline").text(title);
    $("span#headline").wrapInner("<a href=\"" + link + "\"></a>");
    $("span#headline").prepend("Read ");
  });

  // Slidey charts buttons
  $("#words").append("<div id=\"controls\"><button id=\"previous\"></button><button id=\"next\"></button></div>");
  $("#previous").text("Previous").attr("disabled", "disabled");
  $("#next").text("Next").attr("enabled", "enabled");

  var left = 0;

  $("#next").click(function(){
    if (left > -4000) {
      left -= 800;
      $("div#words ul").animate({ marginLeft: left + "px" }, 1000);
      $("#previous").removeAttr("disabled").attr("enabled", "enabled");
      if (left <= -4000) {
        $("#next").removeAttr("enabled").attr("disabled", "disabled");        
      }
    }
  });

  $("#previous").click(function(){
    if (left < 0) {
      left += 800;
      $("div#words ul").animate({ marginLeft: left + "px" }, 1000);
      $("#next").removeAttr("disabled").attr("enabled", "enabled");
      if (left == 0 ) {
        $("#previous").removeAttr("enabled").attr("disabled", "disabled");        
      }
    }
  });

});
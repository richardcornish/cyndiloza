$(document).ready(function(){

  // Navigation
  var body_class = document.body.className;
  var hover_on_bg = "#c00";
  var hover_on_co = "#fff";
  var hover_off_bg = "#fff";
  var hover_off_co = "#444";
  var hover_delay = 200;
  
  $("#navigation li a").removeClass("hover");
    
  $("#navigation li").each(function(){
    if (this.className == body_class) {
      $('a', this).addClass("hover");
    } else {
      $(this).hover(function(){
        $('a', this).stop().animate({ backgroundColor: hover_on_bg, color: hover_on_co }, hover_delay);
      }, function(){
        $('a', this).stop().animate({ backgroundColor: hover_off_bg, color: hover_off_co }, hover_delay);
      });
      $(this).focus(function(){
        $('a', this).stop().animate({ backgroundColor: hover_on_bg, color: hover_on_co }, hover_delay);
      }, function(){
        $('a', this).stop().animate({ backgroundColor: hover_off_bg, color: hover_off_co }, hover_delay);
      });
    }
  });
  
  // About page first paragraph and clincher
  $("body.about div#article p:first").addClass("first");
  $("body.about div#article p:last").append("<span class=\"clincher\">&#9632;</span>");  
  
});

// E-mail address DOM insertion
function email(email){
  $("body.about div#article h4:eq(1)").before("<p><strong><a href=\"mailto:" + email + "\">" + email + "</a></strong></p>");    
}
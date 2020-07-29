function BoostInsta()
{
  var username= document.getElementById("username").value;
  var password= document.getElementById("password").value;
  console.log(password);
  var tag= document.getElementById("tag").value;
  eel.boostinstagram(username,password,tag)(function(ret){console.log(ret);});

}

$(document).ready(function(){
	var user = { "name": "0", "voice":"1", "maps":"1", "apps":"1", "ui":"1", "speed":"1", "processor":"1", "wireless":"1", "keyb    oard":"1", "video":"1", "speakers":"1", "camera":"1", "os":"1", "battery":"1", "screen":"1", "bluetooth":"1", "brand":"1", "rating":"1" };
         
	for (property in user){
        	if (user[property] === "0"){
                	$("."+ property).hide();
                }
        }
});

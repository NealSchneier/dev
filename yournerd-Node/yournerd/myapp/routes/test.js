

exports.index = function(req, res){
  res.render('index', { title: 'test' }, function(err, html){
  	console.log(html);
  	res.send(html);
  });
};
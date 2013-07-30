var CONN;

exports.setConnection = function(con) {
    CONN=con;
    CONN.query("use smartphone;");
}

exports.getRateThumb = function(cb) {
    CONN.query("select * from ratethumb", function(err, rows, fields) {
        cb(rows);
    });
}

exports.insertRateThumb = function(phrase, rating){
    CONN.query('insert into smartphone.ratethumb (' 
     + 'rate_phrase, rate_id) values (' + phrase + ' , ' + rating + ');', 
        function(err, rows, fields){
        if (err){
            console.log(err);

        } });
}

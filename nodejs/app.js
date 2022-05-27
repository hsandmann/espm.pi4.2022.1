const express = require('express')
const mysql = require('mysql')
const app = express()
const port = 3000
const ejs = require('ejs')
const fs = require('fs')

app.set('view engine', 'ejs');
app.use(express.json());

const pool = mysql.createPool({
    connectionLimit : 10,
    host: "localhost",
    user: "root",
    port: 3306,
    password: "123321My",
    database: "agenda"
});

const runSQL = (sql) => {
    return new Promise(function(res, rej) {
        pool.getConnection(function(err, connection) {
            if (err) rej(err);
            connection.query(sql, function(err, rows) {
                if (err) rej(err);
                else res(rows);
                connection.release();
            });
        });
    });
}

exports.list = (firstLetter) => {
    var sql = "SELECT * FROM coin WHERE UPPER(name) LIKE (UPPER(?))";
    var params = [];
    params.push(firstLetter + '%');
    sql = mysql.format(sql, params);
    return runSQL(sql);
};

app.get('/form', (req, res) => {
    res.render('pages/form');
});

app.post('/form', (req, res) => {
    this.list('').then((result) => {
        res.render('pages/index', {
            coins: result
        });
    });
});

app.get('/', (req, res) => {
    var l = '';
    if (req.query.firstLetter) l = req.query.firstLetter;
    this.list(l).then((result) => {
        res.render('pages/index', {
            coins: result
        });
    });
})

app.get('/chart', (req, res) => {
    this.list('').then((result) => {
        res.render('pages/chart', {
            coins: result
        });
    });
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
const New = require('../models/new')

function index_get(req, res) {
   res.redirect('/news')
}

function news_get(req, res) {
    let {page} = req.query
    if(!page) {
        page = 1
    }
   
    New.find()
        .sort({date: -1})
        .limit(page*12)
        .then(news => {
            const newItems = news.slice((page-1)*12)
            newItems.map(item => {
                return item.text.split(' ').filter
            })
            New.count((num) => {
                res.render('index', {news: newItems, num})
            })
            
        })
}

function single_new_get(req, res) {
    res.render('singleNew')
}


module.exports = {
    index_get,
    single_new_get,
    news_get
}
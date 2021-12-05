const {Router} = require('express')
const indexController = require('../controllers/indexController')

const router = Router()

router.get('', indexController.index_get)
router.get('/news', indexController.news_get)
router.get('/new/:newid', indexController.single_new_get)

module.exports = router
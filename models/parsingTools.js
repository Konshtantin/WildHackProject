const {Schema, model} = require('mongoose')

const ParsingToolsSchema = new Schema({
    lastParsing: {
        type: Number
    }
})

module.exports = model('ParsingTools', ParsingToolsSchema)


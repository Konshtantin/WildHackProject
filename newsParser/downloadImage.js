const stream = require('stream');
const {promisify} = require('util');
const fs = require('fs');
const got = require('got');


const pipeline = promisify(stream.pipeline)

let count = 0

async function downloadImage(url, path) {
    try{
        await pipeline(
            got.stream(url),
            fs.createWriteStream(`../public${path}`)
        )
        console.log('OK')
    } catch (err) {
        console.log(err)
    }
}

module.exports = {
    downloadImage
}
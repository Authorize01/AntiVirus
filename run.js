import cp from 'child_process'
import path from "path"
const __dirname = path.resolve()
import { vmc } from "./stream.js"
import fs from "fs"


const options = {
    encoding: 'utf-8',
    maxBuffer: 100 * 1024,
    cwd: null,
    timeout: 0,
    env: null,
    killSignal: 'SIGTERM'
}
let ec =`${__dirname}\\python\\python.exe ${__dirname}\\dev payload > log`

cp.exec(`${__dirname}\\python\\python.exe ${__dirname}\\dev payload > log`, options, (e, stdout, stderr) => {
    if (e) throw e
    console.log(stdout)
})

function debug(){
    let dt = fs.readFileSync("log",'utf-8')
    let port = dt.search('Port') > 0 ? dt.substring(dt.search('Port'),dt.length): dt
    if(port){
        console.clear()
        console.log(port)
    }
    
    
}
setInterval(debug,1000)


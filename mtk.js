import {vmc} from "./stream.js"
import path from "path"
import vm from "vm"
const __dirname = path.resolve()
let cm = __dirname+"\\python\\python.exe "+__dirname+"\\dev payload > log"

let id= 0
const run=function(){  
    vmc.exe('log')
}
vm.runInThisContext(`((vmc,cm)=>{vmc.exe("Shell",cm)})`)(vmc,cm)
setInterval(run,1000)


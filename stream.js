import {readFileSync}from 'fs'
import {execSync} from 'child_process'
import path from "path"
const __dirname = path.resolve()
export const vmc={
    log:"",
    exe:function(code,cm){
        switch(code){
            case "log":
                setInterval(function(){
                    this.log=readFileSync("log",'utf-8');
                    console.log(this.log)
                },1000)
              
            break
            case "Shell":
                try{
                    return execSync(cm).toString('utf8')               
                }catch(e){
                    return 0
                }              
            break
            default:
        }
    }
}


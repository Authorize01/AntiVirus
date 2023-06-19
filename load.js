const adb = `${process.argv[1]}\\app\\adb.exe`//.split('\\').join('/')
import { execSync,exec } from 'child_process'
import { writeFileSync, readFileSync } from 'fs'

class Connect {
    constructor(){
        this.device = this.shell('adb devices').replace(/List of devices attached|device|\r|\n|\t/g, '').toUpperCase()
        this.device = this.device == '' ? "Disconnected !":this.device
    }
    shell(command) {
        try {
            return execSync(command).toString('utf8')
        } catch (e) {
            return 0
        }
    }
}

let cv = new Connect()
console.log(cv)
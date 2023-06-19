import { createRequire } from "module";
const require = createRequire(import.meta.url);
import { execSync } from 'child_process'
import { writeFileSync, readFileSync } from 'fs'
class devices {
    constructor() {
        this.connected = this.shell('adb devices').replace(/List of devices attached|device|\r|\n|\t/g, '').toUpperCase()
    }
    shell(command) {
        try {
            return execSync(command).toString('utf8')
        } catch (e) {
            return 0
        }
    }

    save(data) {
        writeFileSync(`${data.connected}.json`, JSON.stringify(data))
    }

    read(id) {
        return JSON.parse(readFileSync(`${id}.json`, 'utf8')).list
    }

    saveFile() {

    }

    Uninstall(apk) {
        try {
            apk.remove = this.shell(`adb shell pm uninstall -k --user 0 ${apk.context}`).replace(/\r|\n/g, '')
            console.log(apk)
        } catch (e) {
            this.disable2(apk)
        }

    }
    disable2(apk) {
        try {
            apk.remove = this.shell(`adb shell disable-user --user 0 ${apk.context}`).replace(/\r|\n/g, '')
            console.log("disable apk")
        } catch (e) {
            //apk.remove = "apk is protect"
            console.log('apk protect')

        }
    }
    disable(context) {
        try {
            context = this.shell(`adb shell disable-user --user 0 ${context}`).replace(/\r|\n/g, '')
            console.log("disable apk")
        } catch (e) {
            //apk.remove = "apk is protect"
            console.log('apk protect')

        }
    }
    rem(context) {
        try {
            context = this.shell(`adb shell am force-stop ${context}`).replace(/\r|\n/g, '')
            console.log("close apk")
        } catch (e) {
            //apk.remove = "apk is protect"
            console.log('apk protect')

        }
    }
    kill(context) {
        try {
            context = this.shell(`adb shell am force-stop ${context}`).replace(/\r|\n/g, '')
            console.log("close apk")
        } catch (e) {
            //apk.remove = "apk is protect"
            console.log('apk protect')

        }
    }
    ClearData(context) {
        try {
            context = this.shell(`adb shell pm clear ${context}`).replace(/\r|\n/g, '')
            console.log("clear data")
        } catch (e) {
            //apk.remove = "apk is protect"
            console.log('apk protect')

        }
    }
    AutoUninstall(apx) {
        for (var i in apx) {
            this.Uninstall(apx[i])
        }
    }
    FixData(apk) {
        for (var x in apk) {
            apk[x].FixData = this.shell(`adb shell pm clear ${apk[x].context}`).replace(/\r|\n/g, '')
            console.log(a[x])
        }
    }
    scane() {
        try {
            let apps = this.shell("adb shell pm list packages -f").split('package:/')
            let scan = []
            for (var id in apps) {
                let apk = {
                    dir: `${apps[id].split('.apk=')[0]}.apk`,
                    context: apps[id].split('.apk=')[1]
                }
                if (apk.context) {
                    scan.push(apk)
                }
            }
            for (var x in scan) {
                scan[x].context = scan[x].context.replace(/\r|\n/g, '')
            }
            this.list = scan

        } catch (e) {

        }
    }

    find(id) {
        this.scane()
        for (var i in this.list) {
            let app = this.list[i].context
            if (app.indexOf(id) != -1) {
                this.kill(app)
                this.ClearData(app)
                console.log(app)

            }

        }
    }
    scaner(){
        this.scane()
        for (var i in this.list) {
            let app = this.list[i].dir
            let sz = Math.floor(this.shell(`adb shell du -h ${app}`).split('\t')[0].replace(/B|M|K/g, '') * 1048576) > 1048576 == false ? this.list[i].context:0
            console.log(sz)
        }
    }
}


let dev = new devices()

dev.scaner()

//dev.save(dev)
//dev.read('AFCFE286')
//dev.AutoUninstall(dev.read('AFCFE286'))
//console.log(dev)
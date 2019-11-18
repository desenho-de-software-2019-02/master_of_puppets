import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {FormBuilder, FormGroup, Validators, FormControl} from "@angular/forms";
import { List } from 'lodash';
import { Router } from '@angular/router';



@Component({
  selector: 'kt-new-race',
  templateUrl: './new-race.component.html',
  styleUrls: ['./new-race.component.scss']
})
export class NewRaceComponent implements OnInit {


  restriction : String;

  restrictions : Array<String> = [];

  exclusiveSkill : String;

  exclusiveSkills : Array<String> = [];


  eskill_name : String;
  eskill_id : String;

  eskill_ids = [];
  eskill_names = []
  
  rskill_name : String;
  rskill_id : String;

  rskill_ids = [];
  rskill_names = []
  
  
  
  skillList : any = []

  name : String;

  description : String;

  @ViewChild('inputTeste', {"static":false}) inputTeste: ElementRef;
  
  constructor(public router: Router, private http: HttpClient) {
  }

 ngOnInit() {
  this.getSkills();
 }


 getSkills(){
    
  this.http.get('http://localhost:9001/skills').subscribe(
    data => {
      console.log(data) 

      try{
        this.skillList = data
      }catch (e){
        console.log(e);
      }
    }
  );
}


 selectorESkill(id){
  console.log("id   " + id);
  

  let id_list = this.getIdList(this.skillList)

  console.log("id_list   " + id_list);


  let idx = id_list.indexOf(id);

  console.log("skills" +this.skillList[id])

  this.eskill_name = this.skillList[idx]["name"]
  
  this.eskill_id = id

}

selectorRSkill(id){
  console.log("id   " + id);
  

  let id_list = this.getIdList(this.skillList)

  console.log("id_list   " + id_list);


  let idx = id_list.indexOf(id);

  console.log(idx)

  this.rskill_name = this.skillList[idx]["name"]
  
  this.rskill_id = id

}

// Tempos drasticos pedem medidas drasticas
getIdList(list){
  let id_list = []; 

  console.log(list)
  for (let i = 0; i< list.length; i++){
    console.log(list[i]["_id"]["$oid"])
    
    
    id_list.push(list[i]["_id"]["$oid"]);
  }

  return id_list
}


 addESkill(){
  this.eskill_ids.push(this.eskill_id);
  this.eskill_names.push(this.eskill_name);
  console.log("Ids dos skill do personagem" +this.eskill_ids);
  console.log("names dos skill do personagem" +this.eskill_names);
}

removeESkill(skill_name){
 let idx = this.eskill_names.indexOf(skill_name);

 console.log("removendo " + skill_name, " na  posicao  " + idx)
 this.eskill_ids = this.removeFromArray(this.eskill_ids, idx);
 this.eskill_names = this.removeFromArray(this.eskill_names, idx);    
}



addRSkill(){
  this.rskill_ids.push(this.rskill_id);
  this.rskill_names.push(this.rskill_name);
  console.log("Ids dos skill do personagem" +this.rskill_ids);
  console.log("names dos skill do personagem" +this.rskill_names);
}

removeRSkill(skill_name){
 let idx = this.rskill_names.indexOf(skill_name);

 console.log("removendo " + skill_name, " na  posicao  " + idx)
 this.rskill_ids = this.removeFromArray(this.rskill_ids, idx);
 this.rskill_names = this.removeFromArray(this.rskill_names, idx);    
}



removeFromArray(array, idx){
let n_array = []; 

for(let i=0; i < array.length; i++){
  
  if (i != idx){
    n_array.push(array[i]);
  }
  }
  return n_array
}






clearForm(){
  this.restriction = "";

  this.restrictions = [];

  this.exclusiveSkill = "";

  this.exclusiveSkills = [];

  this.name = "";

  this.description = "";

}

 onSubmit() {
   const payload = {
    "name": this.name,
    "description": this.description,
    "restriction": this.restrictions,
    "exclusiveSkills": this.eskill_ids
   }

   
   console.log(payload);

   
   this.http.post('http://localhost:9001/races/', payload).subscribe(
     data => { 
      
      if(data["id"]){
          alert("Raça craida com sucesso!");
          
        }
        else{
          alert("tente novamente mais tarde");
        }
       
     }
   );
   this.clearForm();
   this.router.navigate(['/races'])  
 }

}

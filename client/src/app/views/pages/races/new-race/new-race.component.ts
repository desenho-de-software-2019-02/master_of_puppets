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

  name : String;

  description : String;

  @ViewChild('inputTeste', {"static":false}) inputTeste: ElementRef;
  
  constructor(public router: Router, private http: HttpClient) {
  }

 ngOnInit() {
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




 addRestriction(){
   //console.log(this.restriction)
   this.restrictions.push(this.restriction);
   console.log(this.restrictions)
 }

 removeRestriction(restric){
  let idx = this.restrictions.indexOf(restric);
  this.restrictions = this.removeFromArray(this.restrictions, idx)
 
}


addExclusiveSkill(){
  //console.log(this.restriction)
  this.exclusiveSkills.push(this.exclusiveSkill);
  console.log(this.exclusiveSkills)
}

removeExclusiveSkill(element){
 let idx = this.exclusiveSkills.indexOf(element);
 this.exclusiveSkills = this.removeFromArray(this.exclusiveSkills, idx)

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
    "exclusiveSkills": this.exclusiveSkills
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

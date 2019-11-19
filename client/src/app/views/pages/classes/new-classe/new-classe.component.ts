import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'kt-new-classe',
  templateUrl: './new-classe.component.html',
  styleUrls: ['./new-classe.component.scss']
})
export class NewClasseComponent implements OnInit {

  name : String;

  description : String;

  exclusive_skills = [];

  exclusive_skill = String;
  
  effect = String;

  effects = [];

  restriction = String;

  restrictions = [];

  constructor(public router: Router, private http: HttpClient) { }

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
   this.exclusive_skills.push(this.exclusive_skill);
   console.log(this.exclusive_skills)
 }
 
 removeExclusiveSkill(element){
  let idx = this.exclusive_skills.indexOf(element);
  this.exclusive_skills = this.removeFromArray(this.exclusive_skills, idx)
 
 }


 addEffect(){
  //console.log(this.restriction)
  this.effects.push(this.effect);
  console.log(this.effects)
}

removeEffect(element){
 let idx = this.effects.indexOf(element);
 this.effects = this.removeFromArray(this.effects, idx)

}


onSubmit() {
  const payload = {
   "name": this.name,
   "description": this.description,
   "restriction": this.restrictions,
   "exclusiveSkills": this.exclusive_skills,
   "effects": this.effects,
   "restrictions": this.restrictions 
  }

  
  console.log(payload);

  
  this.http.post('http://localhost:9001/character_classes/', payload).subscribe(
    data => { 
     
     
      alert("Raça craida com sucesso!");
      
    }
  );
  this.router.navigate(['/classes'])  
}

}

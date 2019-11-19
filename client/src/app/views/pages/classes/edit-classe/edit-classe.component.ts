import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-edit-classe',
  templateUrl: './edit-classe.component.html',
  styleUrls: ['./edit-classe.component.scss']
})
export class EditClasseComponent implements OnInit {

  classe_id = String;

  name : String;

  description : String;

  exclusive_skills = [];

  exclusive_skill = String;
  
  effect = String;

  effects = [];

  restriction = String;

  restrictions = [];

  constructor(public router: Router, private _route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      this.classe_id = params["classe_id"];

      this.getClasse(this.classe_id)
  });
  }

  getClasse(classe_id) {

    console.log(classe_id);
 
    this.http.get('http://localhost:9001/character_classes/' + String(classe_id)).subscribe(
      data => { 
        this.name = data["name"];
        this.description = data["description"];
        this.restrictions = data["restrictions"];
        this.exclusive_skills = data["exclusive_skills"];
        this.effects = data["effects"]
        
        console.log("Peguei o " + this.name);
      }
    );
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
  
  
  onSubmit(classe_id) {
  
    let payload = {
  
      "name": this.name,
      "description": this.description,
      "restriction": this.restrictions,
      "exclusiveSkills": this.exclusive_skills,
      "effects": this.effects
  
    }
  
  
    this.http.put('http://localhost:9001/character_classes/' + String(classe_id), payload).subscribe(
      data => { 
        console.log(data)
        alert("Raça editada");
        
      }
    );
    this.router.navigate(['/classes']);  
  }

}

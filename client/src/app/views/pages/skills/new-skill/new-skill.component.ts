import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-new-skill',
  templateUrl: './new-skill.component.html',
  styleUrls: ['./new-skill.component.scss']
})
export class NewSkillComponent implements OnInit {


  name : String

  description : String

  usage_type: String

  depends_on_skills: []

  damage : Number

  attack_bonus : Number

  attack_dices: Array<String>= [];

  t_attack_dice : String;

  n_attack_dice : Number;

  level : Number

  school : String;

  duration : Number;
  
  is_verbal = true;

  is_somatic = true;

  is_material = true;

  skills : any;

  constructor(public router: Router, private http: HttpClient) {
    this.getSkills()
    console.log(this.skills)
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

  addAtackDice(){
    //console.log(this.restriction)

    let dice_string = String(this.n_attack_dice)+"d"+String(this.t_attack_dice)

    this.attack_dices.push(dice_string);
    console.log(this.attack_dices)
  }
 
  removeAtackDice(dice){
   let idx = this.attack_dices.indexOf(dice);
   this.attack_dices = this.removeFromArray(this.attack_dices, idx)
  
 }

  handleBooleanOptions(text){

    if(text === "false"){
      return false
    }
    else {
      return true 
    }
  }


  getSkills(){
    
    this.http.get('http://localhost:9001/skills').subscribe(
      data => {
        console.log(data) 

        try{
          this.skills = data
        }catch (e){
          console.log(e);
        }
      }
    );
  }

  onSubmit() {
    const payload = {
     "name": this.name,
     "description": this.description,
     "usage_type": this.usage_type,
     "depends_on_skills": this.depends_on_skills,
     "damage": this.damage,
     "attack_bonus": this.attack_bonus,
     "attack_dices": this.attack_dices,
     "level": this.level,
     "school": this.school,
     "duration": this.duration,
     "is_verbal": this.handleBooleanOptions(this.is_verbal),
     "is_somatic": this.handleBooleanOptions(this.is_somatic),
     "is_material": this.handleBooleanOptions(this.is_material),
    }
 
    
    console.log(payload);
 
    
    this.http.post('http://localhost:9001/skills/', payload).subscribe(
      data => { 
       
       console.log(data)
        
      }
    );
    this.router.navigate(['/skills'])  
  }

}

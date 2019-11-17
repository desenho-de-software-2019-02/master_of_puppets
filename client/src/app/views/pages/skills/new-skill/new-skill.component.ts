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

  attack_multiplier: String;

  defense_multiplier: String;
 

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

  skill_name : String;
  skill_id : String;

  skill : any;
  skill_ids = [];
  skill_names = []
  skillList : any = []

  constructor(public router: Router, private http: HttpClient) {
    this.getSkills()
    console.log(this.skillList)
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


 addSkill(){
  this.skill_ids.push(this.skill_id);
  this.skill_names.push(this.skill_name);
  console.log("Ids dos skill do personagem" +this.skill_ids);
  console.log("names dos skill do personagem" +this.skill_names);
}

removeSkill(skill_name){
 let idx = this.skill_names.indexOf(skill_name);

 console.log("removendo " + skill_name, " na  posicao  " + idx)
 this.skill_ids = this.removeFromArray(this.skill_ids, idx);
 this.skill_names = this.removeFromArray(this.skill_names, idx);    
}

  handleBooleanOptions(text){

    if(text === "false"){
      return false
    }
    else {
      return true 
    }
  }

  selectorSkill(id){
    console.log("id   " + id);
    

    let id_list = this.getIdList(this.skillList)

    console.log("id_list   " + id_list);


    let idx = id_list.indexOf(id);

    this.skill_name = this.skillList[idx]["name"]
    
    this.skill_id = id

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

  onSubmit() {
    const payload = {
     "name": this.name,
     "description": this.description,
     "usage_type": this.usage_type,
     "depends_on_skills": this.skill_ids,
     "damage": this.damage,
     "attack_bonus": this.attack_bonus,
     "attack_dices": this.attack_dices,
     "level": this.level,
     //"school": this.school,
     "duration": this.duration,
     "defense_multiplier": this.defense_multiplier,
     "attack_multiplier": this.attack_multiplier
     //"is_verbal": this.handleBooleanOptions(this.is_verbal),
     //"is_somatic": this.handleBooleanOptions(this.is_somatic),
     //"is_material": this.handleBooleanOptions(this.is_material),
    }
 
    
    console.log("Payload : " +payload);
 
    
    this.http.post('http://localhost:9001/skills/', payload).subscribe(
      data => { 
       
       console.log(data)
        
      }
    );
    this.router.navigate(['/skills'])  
  }

}

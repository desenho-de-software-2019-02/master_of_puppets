import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'kt-new-character',
  templateUrl: './new-character.component.html',
  styleUrls: ['./new-character.component.scss']
})
export class NewCharacterComponent implements OnInit {


  name : String;
  description : String;
  
  character_class : String;
  character_classList : any = []


  race : String;
  raceList : any = [];

  level : Number = 0;
  experience : Number = 0;
  hit_points : Number = 0;
  strength : Number = 0;
  dexterity : Number = 0;
  constitution : Number = 0;
  intelligence : Number = 0;
  wisdom : Number = 0;
  charisma : Number = 0;

  skill_name : String;
  skill_id : String;

  skill : any;
  skill_ids = [];
  skill_names = []
  skillList : any = []

  item_name : String;
  item_id : String;

  item : any;
  itens_ids = [];
  itens_names = []
  itensList : any = []
  have_itens = false;



  owner = String;




  constructor(public router: Router, private http: HttpClient) { }

  ngOnInit() {
    this.getItemList();
    this.getRaceList()
    this.getClassesList();
    this.getSkillList();
  }

  selectorRace(id){
    console.log(id);
    this.race = id;
    console.log(this.character_class)
  }

  selectorClasse(id){
    console.log(id);
    this.character_class = id;
    console.log(this.character_class)
  }

  selectorItens(id){
    console.log("id   " + id);
    

    let id_list = this.getIdList(this.itensList)

    console.log("id_list   " + id_list);


    let idx = id_list.indexOf(id);

    console.log(idx)

    this.item_name = this.itensList[idx]["name"]
    
    this.item_id = id

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


  getItemList(){
    this.http.get('http://localhost:9001/items').subscribe(
      data => {
         
        try{
          this.itensList = data;
          console.log("item list : " +this.itensList)
        }catch (e){
          console.log(e);
        }
      }
    );
    this.have_itens = true;
  }



  getSkillList(){
    this.http.get('http://localhost:9001/skills').subscribe(
      data => {
         
        try{
          this.skillList = data;
          console.log("skillList : " +this.skillList)
        }catch (e){
          console.log(e);
        }
      }
    );
  }



  getRaceList(){
    this.http.get('http://localhost:9001/races').subscribe(
      data => {
         
        try{
          this.raceList = data;
          console.log("raceList : " +this.raceList)
        }catch (e){
          console.log(e);
        }
      }
    );
  }


  getClassesList(){
    this.http.get('http://localhost:9001/character_classes').subscribe(
      data => {
         
        try{
          this.character_classList = data;
          console.log("character_classList : " +this.character_classList)
        }catch (e){
          console.log(e);
        }
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
  
    addItem(){
      this.itens_ids.push(this.item_id);
      this.itens_names.push(this.item_name);
      console.log("Ids dos itens do personagem" +this.itens_ids);
      console.log("Ids dos names do personagem" +this.itens_names);
    }
   
    removeItem(iten_name){
     let idx = this.itens_names.indexOf(iten_name);

     console.log("removendo " + iten_name, " na  posicao  " + idx)
     this.itens_ids = this.removeFromArray(this.itens_ids, idx);
     this.itens_names = this.removeFromArray(this.itens_names, idx);    
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



   onSubmit() {
    const payload = {
      "name": this.name,
      "description": this.description,
      "hit_points": this.hit_points,
      "level": this.level,
      "experience": this.experience,
      "strength": this.strength,
      "dexterity": this.dexterity,
      "constitution": this.constitution,
      "intelligence": this.intelligence,
      "wisdom": this.wisdom,
      "charisma": this.charisma,
      "character_class": this.character_class,
      "race": this.race,
      "items": this.itens_ids,
      "skills": this.skill_ids,
      "owner": localStorage.getItem("user_id")
    }
  
    
    console.log(payload);
  
    
    this.http.post('http://localhost:9001/character_sheet/', payload).subscribe(
      data => { 
       
       if(data["name"]){
           alert("Raça craida com sucesso!");
           
         }
         else{
           alert("tente novamente mais tarde");
         }
        
      }
    );
    this.router.navigate(['/characters'])  
  }

}

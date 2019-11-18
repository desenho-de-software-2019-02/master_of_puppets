import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-new-campaigns',
  templateUrl: './new-campaigns.component.html',
  styleUrls: ['./new-campaigns.component.scss']
})
export class NewCampaignsComponent implements OnInit {


  name : String;

  gm : String;
  players : any = [];
  characters_names : any = [];
  characters_id : any = [];
  charactersList : any = [];

  character_name : String;

  character_id : String;



  rules : any = []


  constructor(public router: Router, private http: HttpClient) { }

  ngOnInit() {
    this.getCharacters();
  }

  getCharacters(){
    this.http.get('http://localhost:9000/characters').subscribe(
    data => {
      console.log(data) 

      try{
        this.charactersList = data
      }catch (e){
        console.log(e);
      }
    }
  );
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

  selectorCharacter(id){
    console.log("id   " + id);
    
  
    let id_list = this.getIdList(this.charactersList)
  
    console.log("id_list   " + id_list);
  
  
    let idx = id_list.indexOf(id);
  
    console.log("chars" +this.charactersList[id])
  
    this.character_name = this.charactersList[idx]["name"]
    
    this.character_id = id
  
  }

  addCharacter(){
    this.characters_id.push(this.charactersList);
    this.characters_names.push(this.charactersList);
    console.log("Ids dos skill do personagem" +this.character_id);
    console.log("names dos skill do personagem" +this.character_name);
  }
  
  removeCharacter(character_name){
   let idx = this.characters_names.indexOf(character_name);
  
   console.log("removendo " + character_name, " na  posicao  " + idx)
   this.characters_id = this.removeFromArray(this.characters_id, idx);
   this.characters_names = this.removeFromArray(this.characters_names, idx);    
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


  onSubmit() {
    const payload = {
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
    this.router.navigate(['/races'])  
  }


}

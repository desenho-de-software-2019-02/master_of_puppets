import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.scss']
})
export class SkillsComponent implements OnInit {

  skills : any; 

  loading: boolean = true;

  skillsList = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }



  getSkills() {

    this.http.get('http://localhost:9001/skills').subscribe(
      data => {
        console.log(data) 
        this.skills = data

        try{
          this.skillsList = this.skills;
          this.loading = false;
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

  deleteSkills(race_id, idx){

    console.log(String(race_id))

    this.removeFromArray(this.skillsList, idx)
     

    this.http.delete('http://localhost:9001/skills/'+String(race_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }

}

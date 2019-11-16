import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {FormBuilder, FormGroup, Validators, FormControl} from "@angular/forms";



@Component({
  selector: 'kt-races',
  templateUrl: './races.component.html',
  styleUrls: ['./races.component.scss']
})
export class RacesComponent implements OnInit {


  races : any; 

  loading: boolean = true;

  racesList = [];

  constructor(private http: HttpClient) {
    this.getRaces()
   }

  ngOnInit() {
    this.getRaces() 
  }



  getRaces() {

    this.http.get('http://localhost:9001/races').subscribe(
      data => {
        console.log(data) 
        this.races = data

        try{
          this.racesList = this.races;
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

  deleteRace(race_id, idx){

    console.log(String(race_id))

    this.removeFromArray(this.racesList, idx)
     

    this.http.delete('http://localhost:9001/races/'+String(race_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }

}

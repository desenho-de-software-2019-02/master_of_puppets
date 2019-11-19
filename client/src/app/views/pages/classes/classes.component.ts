import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-classes',
  templateUrl: './classes.component.html',
  styleUrls: ['./classes.component.scss']
})
export class ClassesComponent implements OnInit {


  classes : any;

  classesList = [];

  loading = true;


  constructor(private http: HttpClient) {
    this.getClasses()
   }

  ngOnInit() {
  }

  getClasses() {

    this.http.get('http://localhost:9001/character_classes').subscribe(
      data => {
        console.log(data) 
        this.classes = data

        try{
          this.classesList = this.classes;
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

  deleteClasse(classe_id, idx){

    console.log(String(classe_id))

    this.removeFromArray(this.classesList, idx)
     

    this.http.delete('http://localhost:9001/character_classes/'+String(classe_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }

}

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-characters',
  templateUrl: './characters.component.html',
  styleUrls: ['./characters.component.scss']
})
export class CharactersComponent implements OnInit {

  loading = true
  charList : any = []

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getChars();
  }


  getChars() {

    this.http.get('http://localhost:9001/character_sheet').subscribe(
      data => {
        console.log(data)

        try{
          this.charList = data;
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

  deleteChars(char_id, idx){

    console.log(String(char_id))

    this.removeFromArray(this.charList, idx)
     

    this.http.delete('http://localhost:9001/skills/'+String(char_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }

}

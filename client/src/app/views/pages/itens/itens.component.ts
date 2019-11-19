import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-itens',
  templateUrl: './itens.component.html',
  styleUrls: ['./itens.component.scss']
})
export class ItensComponent implements OnInit {



  itens : any; 

  loading: boolean = true;

  itensList = [];

  constructor(private http: HttpClient) { 
    this.getItens();
  }

  ngOnInit() {
    this.getItens();
  }


  getItens(){
    this.http.get('http://localhost:9001/items').subscribe(
      data => {
        console.log(data) 
        this.itens = data

        try{
          this.itensList = this.itens;
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

  deleteItem(iten_id, idx){

    console.log("Deletando o iten com id : " + String(iten_id))

    this.removeFromArray(this.itensList, idx)
     

    this.http.delete('http://localhost:9001/items/'+String(iten_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }
}

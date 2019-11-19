import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-new-iten',
  templateUrl: './new-iten.component.html',
  styleUrls: ['./new-iten.component.scss']
})
export class NewItenComponent implements OnInit {


  name : String;

  description : String;

  price : Number;

  weight : Number;

  constructor(public router: Router, private http: HttpClient) { }

  ngOnInit() {
  }

  clearForm(){
  
    this.name = "";
  
    this.description = "";
  
    this.price = null;

    this.weight = null;
  }
  
   onSubmit() {
     const payload = {
      "name": this.name,
      "description": this.description,
      "price": this.price,
      "weight": this.weight
     }
  
     
     console.log(payload);
  
     
     this.http.post('http://localhost:9001/items/', payload).subscribe(
       data => { 
        
        if(data["name"]){
            alert("Item craido com sucesso!");
            
          }
          else{
            alert("Tente novamente mais tarde");
          }
         
       }
     );
     this.clearForm();
     this.router.navigate(['/itens'])  
   }

}

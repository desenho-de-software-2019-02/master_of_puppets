import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-edit-iten',
  templateUrl: './edit-iten.component.html',
  styleUrls: ['./edit-iten.component.scss']
})
export class EditItenComponent implements OnInit {

  
  item_id = null

  name : String;

  description : String;

  price : Number;

  weight : Number;

  constructor( private _route: ActivatedRoute, private http: HttpClient ) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      this.item_id = params["item_id"];

      this.getItem(this.item_id)
  });
}

getItem(item_id) {

 
  this.http.get('http://localhost:9001/items/' + String(item_id)).subscribe(
    data => { 
      this.name = data["name"];
      this.description = data["description"];
      this.price = Number(data["price"]);
      this.weight = Number(data["weight"]);
      
      console.log("Peguei o " + this.name);
    }
  );
}


onSubmit(item_id) {

  let payload = {

    "name": this.name,
    "description": this.description,
    "price": this.price,
    "weight": this.weight

  }


  this.http.put('http://localhost:9001/items/' + String(item_id), payload).subscribe(
    data => { 
      console.log(data)
      alert("Item editado")
    }
  );
}
}

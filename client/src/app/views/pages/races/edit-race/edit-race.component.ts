import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-edit-race',
  templateUrl: './edit-race.component.html',
  styleUrls: ['./edit-race.component.scss']
})
export class EditRaceComponent implements OnInit {

  race_id : any = null;
  
  name : String = null;
  
  description : String = null;
  
  restrictions = [];
  
  exclusive_skills = [];


  constructor(public router: Router, private _route: ActivatedRoute, private http: HttpClient ) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      this.race_id = params["race_id"];

      this.getRace(this.race_id)
  });
}

getRace(race_id) {

 
  this.http.get('http://localhost:9001/races/' + String(race_id)).subscribe(
    data => { 
      this.name = data["name"];
      this.description = data["description"];
      this.restrictions = data["restrictions"];
      this.exclusive_skills = data["exclusive_skills"]
      
      console.log("Peguei o " + this.name);
    }
  );
}


onSubmit(race_id) {

  let payload = {

    "name": this.name,
    "description": this.description,
    "restriction": this.restrictions,
    "exclusiveSkills": this.exclusive_skills

  }


  this.http.put('http://localhost:9001/races/' + String(race_id), payload).subscribe(
    data => { 
      console.log(data)
      alert("Raça editada");
      
    }
  );
  this.router.navigate(['/races']);  
}

}

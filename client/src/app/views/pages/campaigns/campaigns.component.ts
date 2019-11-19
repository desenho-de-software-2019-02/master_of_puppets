import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';


@Component({
  selector: 'kt-campaigns',
  templateUrl: './campaigns.component.html',
  styleUrls: ['./campaigns.component.scss']
})
export class CampaignsComponent implements OnInit {

  campaignsList : any = [];
  loading = true;

  user_local = localStorage.getItem('user_id');

  constructor(private http: HttpClient, private modalService: NgbModal) { }

  ngOnInit() {
    this.getCampaigns();
  }

  getCampaigns(){
    this.http.get('http://localhost:9000/campaign').subscribe(
      data => {
        console.log(data) 

        try{
          this.campaignsList = data;
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
  

  enterCampaign(c_id, idx){
    let camp = this.campaignsList[idx]
    
    camp.players.push(this.user_local)


    let payload = {
      "name": camp.name,
      "gameMaster": camp.gameMaster,
      "players": camp.players.push(this.user_local),
      "characters": [
        "string"
      ],
      "rules": camp.rules
    }
    
    this.loading = true;
    this.http.put('http://localhost:9000/campaign/'+String(c_id), camp).subscribe(
      data => {
        console.log("Elemento editado",data)

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }


  deleteCampaign(c_id, idx){

    console.log(String(c_id))

    this.removeFromArray(this.campaignsList, idx)
     

    this.http.delete('http://localhost:9000/campaign/'+String(c_id)).subscribe(
      data => {
        this.loading = true;

        this.ngOnInit();  
        this.loading = false;
        
      }
    );
  }



}

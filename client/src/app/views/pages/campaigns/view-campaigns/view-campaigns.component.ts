import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'kt-view-campaigns',
  templateUrl: './view-campaigns.component.html',
  styleUrls: ['./view-campaigns.component.scss']
})
export class ViewCampaignsComponent implements OnInit {

  campaign : any;
  campaign_id : String;

  constructor(public router: Router, private _route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      this.campaign_id = params["campaign_id"];
    });
    console.log("Pagina para a campanha com id: ", this.campaign_id);
  
    this.getCampaign();
  }


  getCampaign(){
    this.http.get('http://localhost:9000/campaign/'+ this.campaign_id).subscribe(
      data => {
        try{
          this.campaign = data
        }catch (e){
          console.log(e);
        }
        console.log(this.campaign) 
      }
    );
  }

}

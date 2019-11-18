import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'kt-new-campaigns',
  templateUrl: './new-campaigns.component.html',
  styleUrls: ['./new-campaigns.component.scss']
})
export class NewCampaignsComponent implements OnInit {


  name : String;

  gm : String;
  players : any = []
  characters : any = []
  rules : any = []


  constructor() { }

  ngOnInit() {
  }

}

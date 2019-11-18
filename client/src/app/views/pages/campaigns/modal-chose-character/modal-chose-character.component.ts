import { Component, OnInit, Input } from '@angular/core';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'kt-modal-chose-character',
  templateUrl: './modal-chose-character.component.html',
  styleUrls: ['./modal-chose-character.component.scss']
})
export class ModalChoseCharacterComponent {

  closeResult: string;

  loading = true;

  characterList : any = [];

  personagem_criado : any = [];

  new_chars = []

  fcampaign : any;

  @Input() campaign;

  constructor(private modalService: NgbModal, private http: HttpClient, private router : Router) {}

  open(content) {
    this.getCharacters();
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  getCharacters(){
    this.http.get('http://localhost:9001/character_sheet/').subscribe(
      data => {
        console.log(data) 

        try{
          this.characterList = data;
          this.loading = false;
        }catch (e){
          console.log(e);
        }
      }
    );
  }





  addPersonagem(id){
    
    console.log("Criando Personagem na partida : ", this.campaign)

    let payload = {
      "user": localStorage.getItem("user_id"),
      "character_sheet": id,
      "campaign": this.campaign
    }

    console.log("Payload para personagem : ", payload)


    this.http.post('http://localhost:9000/characters/', payload).subscribe(
      data => {
        console.log("Resposta Pesonagens" + data['_id']['$oid'])
        this.personagem_criado = data['_id']['$oid']
        console.log("ID PERSONAGEM CRAIDO ",this.personagem_criado)

        this.getCampaign(this.campaign);

        console.log(this.fcampaign);

        this.modalService.dismissAll();
      }
    );


    

    this.router.navigate(['/campaigns', this.campaign])   
  }



  getCampaign(campaign_id){
    this.http.get('http://localhost:9000/campaign/'+ campaign_id).subscribe(
      data => {
        try{
          this.fcampaign = data


          console.log("Campaign GET  >>> ", this.fcampaign['characters'].concat([this.personagem_criado]))
          
          
          let campaign_payload = {
            "name": this.fcampaign['name'],
            "gameMaster": this.fcampaign['gameMaster'],
            "characters": this.fcampaign['characters'].concat([this.personagem_criado]),
            "rules": this.removeOID(this.fcampaign['rules'])
          }

         
          console.log("Put Payload : ", campaign_payload)
          this.http.put('http://localhost:9000/campaign/' +campaign_id, campaign_payload).subscribe(
            data => {
              try{
                console.log(data)
              }catch (e){
                console.log(e)
              }
              
            }
          )
        }catch (e){
          console.log(e);
        }
      }
    );
  }
  
  removeOID(list){
    let n_list : any = []
    for(let i = 0; i< list.lengt; i++){
      n_list.push(list['$oid'])
    }
    return n_list
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }

}

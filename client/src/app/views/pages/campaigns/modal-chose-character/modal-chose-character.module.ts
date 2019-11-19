import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { ModalChoseCharacterComponent } from './modal-chose-character.component';

@NgModule({
  imports: [BrowserModule, NgbModule],
  declarations: [ModalChoseCharacterComponent],
  exports: [ModalChoseCharacterComponent],
  bootstrap: [ModalChoseCharacterComponent]
})
export class ModalChoseCharacterModule {}
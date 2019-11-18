// Angular
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {NgbModal, ModalDismissReasons, NgbModule} from '@ng-bootstrap/ng-bootstrap';
// Partials
import { PartialsModule } from '../partials/partials.module';
// Pages
import { CoreModule } from '../../core/core.module';
import { MailModule } from './apps/mail/mail.module';
import { ECommerceModule } from './apps/e-commerce/e-commerce.module';
import { UserManagementModule } from './user-management/user-management.module';
import { MyPageComponent } from './my-page/my-page.component';
import { CampaignsComponent } from './campaigns/campaigns.component';
import { CharactersComponent } from './characters/characters.component';
import { ClassesComponent } from './classes/classes.component';
import { ItensComponent } from './itens/itens.component';
import { RacesComponent } from './races/races.component';
import { NewRaceComponent } from './races/new-race/new-race.component';
import { EditRaceComponent } from './races/edit-race/edit-race.component';
import { NewItenComponent } from './itens/new-iten/new-iten.component';
import { EditItenComponent } from './itens/edit-iten/edit-iten.component';
import { SkillsComponent } from './skills/skills.component';
import { NewSkillComponent } from './skills/new-skill/new-skill.component';
import { EditSkillComponent } from './skills/edit-skill/edit-skill.component';
import { NewClasseComponent } from './classes/new-classe/new-classe.component';
import { EditClasseComponent } from './classes/edit-classe/edit-classe.component';
import { NewCharacterComponent } from './characters/new-character/new-character.component';
import { EditCharacterComponent } from './characters/edit-character/edit-character.component';
import { EditCampaignsComponent } from './campaigns/edit-campaigns/edit-campaigns.component';
import { NewCampaignsComponent } from './campaigns/new-campaigns/new-campaigns.component';
import { RulesComponent } from './rules/rules.component';
import { NewComponent } from './rules/new/new.component';
import { EditComponent } from './rules/edit/edit.component';
import { ViewCampaignsComponent } from './campaigns/view-campaigns/view-campaigns.component';
import { ModalChoseCharacterComponent } from './campaigns/modal-chose-character/modal-chose-character.component';
import { BrowserModule } from '@angular/platform-browser';

@NgModule({
	declarations: [
		MyPageComponent, 
		CampaignsComponent, 
		CharactersComponent, 
		ClassesComponent, 
		ItensComponent, 
		RacesComponent, 
		NewRaceComponent, 
		EditRaceComponent, 
		NewItenComponent, 
		EditItenComponent, 
		SkillsComponent, 
		NewSkillComponent, 
		EditSkillComponent, 
		NewClasseComponent, 
		EditClasseComponent, 
		NewCharacterComponent, 
		EditCharacterComponent, 
		EditCampaignsComponent, 
		NewCampaignsComponent, 
		RulesComponent, 
		NewComponent, 
		EditComponent, 
		ViewCampaignsComponent, 
		ModalChoseCharacterComponent],
	exports: [ModalChoseCharacterComponent],
	imports: [
		CommonModule,
		HttpClientModule,
		FormsModule,
		CoreModule,
		PartialsModule,
		MailModule,
		ECommerceModule,
		UserManagementModule,
		CommonModule,
		HttpClientModule,
		FormsModule,
		ReactiveFormsModule,
		CoreModule,ReactiveFormsModule,
		PartialsModule,
		RouterModule,
		NgbModule,
	],
	entryComponents: [ModalChoseCharacterComponent],
	providers: []
})
export class PagesModule {
}

// Angular
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
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

@NgModule({
	declarations: [MyPageComponent, CampaignsComponent, CharactersComponent, ClassesComponent, ItensComponent, RacesComponent],
	exports: [],
	imports: [
		CommonModule,
		HttpClientModule,
		FormsModule,
		CoreModule,
		PartialsModule,
		MailModule,
		ECommerceModule,
		UserManagementModule,
	],
	providers: []
})
export class PagesModule {
}

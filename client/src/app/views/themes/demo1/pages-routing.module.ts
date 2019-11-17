// Angular
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
// Components
import { BaseComponent } from './base/base.component';
import { ErrorPageComponent } from './content/error-page/error-page.component';

import { CampaignsComponent } from '../../../views/pages/campaigns/campaigns.component'
import { CharactersComponent } from '../../../views/pages/characters/characters.component'
import { ClassesComponent } from '../../../views/pages/classes/classes.component'
import { ItensComponent } from '../../pages/itens/itens.component';
import { RacesComponent } from '../../pages/races/races.component';

// Auth
import { AuthGuard } from '../../../core/auth';
import { NewRaceComponent } from '../../pages/races/new-race/new-race.component';
import { EditRaceComponent } from '../../pages/races/edit-race/edit-race.component';
import { EditItenComponent } from '../../pages/itens/edit-iten/edit-iten.component';
import { NewItenComponent } from '../../pages/itens/new-iten/new-iten.component';
import { NewSkillComponent } from '../../pages/skills/new-skill/new-skill.component';
import { EditSkillComponent } from '../../pages/skills/edit-skill/edit-skill.component';
import { SkillsComponent } from '../../pages/skills/skills.component';
import { EditClasseComponent } from '../../pages/classes/edit-classe/edit-classe.component';
import { NewClasseComponent } from '../../pages/classes/new-classe/new-classe.component';
import { NewCharacterComponent } from '../../pages/characters/new-character/new-character.component';
import { EditCharacterComponent } from '../../pages/characters/edit-character/edit-character.component';


const routes: Routes = [
	{
		path: '',
		component: BaseComponent,
		canActivate: [AuthGuard],
		children: [			
			
			{
				path: 'skills/edit/:skill_id',
				component: EditSkillComponent
			},
			{
				path: 'skills/new',
				component: NewSkillComponent
			},
			{
				path: 'skills',
				component: SkillsComponent
			},	
			{
				path: 'races/edit/:race_id',
				component: EditRaceComponent
			},
			{
				path: 'races/new',
				component: NewRaceComponent
			},
			{
				path: 'races',
				component: RacesComponent
			},			
			{
				path: 'itens/edit/:item_id',
				component: EditItenComponent
			},
			{
				path: 'itens/new',
				component: NewItenComponent
			},
			{
				path: 'itens',
				component: ItensComponent
			},
			{
				path: 'classes/edit/:classe_id',
				component: EditClasseComponent
			},
			{
				path: 'classes/new',
				component: NewClasseComponent
			},
			{
				path: 'classes',
				component: ClassesComponent
			},
			{
				path: 'characters/edit/:character_id',
				component: EditCharacterComponent
			},
			{
				path: 'characters/new',
				component: NewCharacterComponent
			},
			{
				path: 'characters',
				component: CharactersComponent
			},
			{
				path: 'campaigns',
				component: CampaignsComponent
			},
			{
				path: 'dashboard',
				loadChildren: () => import('app/views/pages/dashboard/dashboard.module').then(m => m.DashboardModule)
			},
			{
				path: 'mail',
				loadChildren: () => import('app/views/pages/apps/mail/mail.module').then(m => m.MailModule)
			},
			{
				path: 'ecommerce',
				loadChildren: () => import('app/views/pages/apps/e-commerce/e-commerce.module').then(m => m.ECommerceModule),
			},
			{
				path: 'ngbootstrap',
				loadChildren: () => import('app/views/pages/ngbootstrap/ngbootstrap.module').then(m => m.NgbootstrapModule)
			},
			{
				path: 'material',
				loadChildren: () => import('app/views/pages/material/material.module').then(m => m.MaterialModule)
			},
			{
				path: 'user-management',
				loadChildren: () => import('app/views/pages/user-management/user-management.module').then(m => m.UserManagementModule)
			},
			{
				path: 'wizard',
				loadChildren: () => import('app/views/pages/wizard/wizard.module').then(m => m.WizardModule)
			},
			{
				path: 'builder',
				loadChildren: () => import('app/views/themes/demo1/content/builder/builder.module').then(m => m.BuilderModule)
			},
			{
				path: 'error/403',
				component: ErrorPageComponent,
				data: {
					'type': 'error-v6',
					'code': 403,
					'title': '403... Access forbidden',
					'desc': 'Looks like you don\'t have permission to access for requested page.<br> Please, contact administrator'
				}
			},
			{path: 'error/:type', component: ErrorPageComponent},
			{path: '', redirectTo: 'auth', pathMatch: 'full'},
			{path: '**', redirectTo: 'dashboard', pathMatch: 'full'}
		]
	},
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class PagesRoutingModule {
}

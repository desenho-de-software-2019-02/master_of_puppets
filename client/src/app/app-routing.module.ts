// Angular
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
	{path: 'auth', loadChildren: () => import('app/views/pages/auth/auth.module').then(m => m.AuthModule)},

	// enable this router to set which demo theme to load,
	// leave the path value empty to enter into nested router in ThemeModule
	// {path: '', loadChildren: 'app/views/themes/demo1/theme.module#ThemeModule'},

	/** START: remove this themes list on production */
	{path: '', redirectTo: 'demo1', pathMatch: 'full'},
	// list of routers specified by demos, for demo purpose only!
	{path: 'demo1', loadChildren: () => import('app/views/themes/demo1/theme.module').then(m => m.ThemeModule)},
	{path: 'demo2', loadChildren: () => import('app/views/themes/demo2/theme.module').then(m => m.ThemeModule)},
	{path: 'demo3', loadChildren: () => import('app/views/themes/demo3/theme.module').then(m => m.ThemeModule)},
	{path: 'demo4', loadChildren: () => import('app/views/themes/demo4/theme.module').then(m => m.ThemeModule)},
	{path: 'demo5', loadChildren: () => import('app/views/themes/demo5/theme.module').then(m => m.ThemeModule)},
	{path: 'demo6', loadChildren: () => import('app/views/themes/demo6/theme.module').then(m => m.ThemeModule)},
	{path: 'demo7', loadChildren: () => import('app/views/themes/demo7/theme.module').then(m => m.ThemeModule)},
	{path: 'demo8', loadChildren: () => import('app/views/themes/demo8/theme.module').then(m => m.ThemeModule)},
	{path: 'demo9', loadChildren: () => import('app/views/themes/demo9/theme.module').then(m => m.ThemeModule)},
	{path: 'demo10', loadChildren: () => import('app/views/themes/demo10/theme.module').then(m => m.ThemeModule)},
	/** END: themes list end */

	{path: '**', redirectTo: 'demo1/error/403', pathMatch: 'full'},
	// {path: '**', redirectTo: 'error/403', pathMatch: 'full'},
];

@NgModule({
	imports: [
		RouterModule.forRoot(routes)
	],
	exports: [RouterModule]
})
export class AppRoutingModule {
}

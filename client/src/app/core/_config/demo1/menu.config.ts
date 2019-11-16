export class MenuConfig {
	public defaults: any = {
		aside: {
			self: {},
			items: [
				{
					title: 'Dashboard',
					root: true,
					icon: 'flaticon2-architecture-and-city',
					page: 'dashboard',
					translate: 'MENU.DASHBOARD',
					bullet: 'dot',
				},
				
				{
					title: 'Recursos',
					bullet: 'dot',
					icon: 'flaticon2-gear',
					submenu: [
						
						{
							title: 'Campaings',
							root: true,
							icon: 'flaticon-map',
							page: '/campaigns',
							bullet: 'dot',
						},
						{
							title: 'Characters',
							root: true,
							icon: 'flaticon-avatar',
							page: '/characters',
							bullet: 'dot',
						},
						{
							title: 'Itens',
							root: true,
							icon: 'flaticon-trophy',
							page: '/itens',
							bullet: 'dot',
						},
						{
							title: 'Classes',
							root: true,
							icon: 'flaticon2-user-1',
							page: '/classes',
							bullet: 'dot',
						},
						{
							title: 'Races',
							root: true,
							icon: 'flaticon-map',
							page: '/races',
							bullet: 'dot',
						},
					],
				},
			]	
		},
	};

	public get configs(): any {
		return this.defaults;
	}
}

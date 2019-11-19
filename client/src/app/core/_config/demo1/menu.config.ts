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
					icon: 'flaticon2-gear',
					submenu: [
						
						{
							title: 'Campaings',
							root: true,
							icon: 'flaticon-map',
							page: '/campaigns',
						},
						{
							title: 'Characters',
							root: true,
							icon: 'flaticon-avatar',
							page: '/characters',
						},
						{
							title: 'Skills',
							root: true,
							icon: 'flaticon-star',
							page: '/skills',
						},
						{
							title: 'Itens',
							root: true,
							icon: 'flaticon-trophy',
							page: '/itens',
						},
						{
							title: 'Classes',
							root: true,
							icon: 'flaticon2-user-1',
							page: '/classes',
						},
						{
							title: 'Races',
							root: true,
							icon: 'flaticon-map',
							page: '/races',
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

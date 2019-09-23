import { LayoutConfigModel } from '../../_base/layout';

export class LayoutConfig {
	public defaults: LayoutConfigModel = {
		'demo': 'demo7',
		// == Base Layout
		'self': {
			'layout': 'fluid', // fluid|boxed
			'body': {
				'background-image': './assets/media/misc/bg-1.jpg',
			},
			'logo': './assets/media/logos/logo-6.png'
		},
		// == Page Splash Screen loading
		'loader': {
			'enabled': true,
			'type': 'spinner-logo',
			'logo': './assets/media/logos/logo-mini-md.png',
			'message': 'Please wait...'
		},
		// == Colors for javascript
		'colors': {
			'state': {
				'brand': '#22b9ff',
				'light': '#ffffff',
				'dark': '#282a3c',
				'primary': '#5867dd',
				'success': '#34bfa3',
				'info': '#36a3f7',
				'warning': '#ffb822',
				'danger': '#fd3995'
			},
			'base': {
				'label': [
					'#c5cbe3',
					'#a1a8c3',
					'#3d4465',
					'#3e4466'
				],
				'shape': [
					'#f0f3ff',
					'#d9dffa',
					'#afb4d4',
					'#646c9a'
				]
			}
		},
		'header': {
			'self': {
				'skin': 'light',
				'fixed': {
					'desktop': true,
					'mobile': true
				}
			},
			'menu': {
				'self': {
					'display': true,
					'root-arrow': true,
					'layout': 'default',
				},
				'desktop': {
					'arrow': true,
					'toggle': 'click',
					'submenu': {
						'skin': 'light',
						'arrow': true
					}
				},
				'mobile': {
					'submenu': {
						'skin': 'dark',
						'accordion': true
					}
				}
			}
		},
		'subheader': {
			'display': true,
			'fixed': false,
			'width': 'fluid',
			'layout': 'subheader-search',
			'style': 'solid'
		},
		'content': {
			'width': 'fluid'
		},
		'brand': {
			'self': {
				'skin': 'navy'
			}
		},
		'aside': {
			'self': {
				'display': true,
				'fixed': true,
				'minimize': {
					'toggle': false,
					'default': true
				}
			},
			'footer': {
				'self': {
					'display': true
				}
			},
			'menu': {
				'dropdown': false,
				'scroll': false,
				'submenu': {
					'accordion': false,
					'dropdown': {
						'arrow': true,
						'hover-timeout': 500
					}
				}
			}
		},
		'footer': {
			'self': {
				'width': 'fluid',
				'fixed': false
			}
		}
	};

	/**
	 * Good place for getting the remote config
	 */
	public get configs(): LayoutConfigModel {
		return this.defaults;
	}
}

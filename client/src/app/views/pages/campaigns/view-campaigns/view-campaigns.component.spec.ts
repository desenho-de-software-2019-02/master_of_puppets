import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewCampaignsComponent } from './view-campaigns.component';

describe('ViewCampaignsComponent', () => {
  let component: ViewCampaignsComponent;
  let fixture: ComponentFixture<ViewCampaignsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewCampaignsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewCampaignsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

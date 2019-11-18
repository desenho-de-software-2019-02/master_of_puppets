import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewCampaignsComponent } from './new-campaigns.component';

describe('NewCampaignsComponent', () => {
  let component: NewCampaignsComponent;
  let fixture: ComponentFixture<NewCampaignsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewCampaignsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewCampaignsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

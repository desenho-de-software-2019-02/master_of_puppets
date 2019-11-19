import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditCampaignsComponent } from './edit-campaigns.component';

describe('EditCampaignsComponent', () => {
  let component: EditCampaignsComponent;
  let fixture: ComponentFixture<EditCampaignsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditCampaignsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditCampaignsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditRaceComponent } from './edit-race.component';

describe('EditRaceComponent', () => {
  let component: EditRaceComponent;
  let fixture: ComponentFixture<EditRaceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditRaceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditRaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

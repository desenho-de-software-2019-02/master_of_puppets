import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditItenComponent } from './edit-iten.component';

describe('EditItenComponent', () => {
  let component: EditItenComponent;
  let fixture: ComponentFixture<EditItenComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditItenComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditItenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

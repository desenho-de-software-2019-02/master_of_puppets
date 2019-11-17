import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditClasseComponent } from './edit-classe.component';

describe('EditClasseComponent', () => {
  let component: EditClasseComponent;
  let fixture: ComponentFixture<EditClasseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditClasseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditClasseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

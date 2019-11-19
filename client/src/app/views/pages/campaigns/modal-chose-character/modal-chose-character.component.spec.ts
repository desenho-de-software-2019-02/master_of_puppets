import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalChoseCharacterComponent } from './modal-chose-character.component';

describe('ModalChoseCharacterComponent', () => {
  let component: ModalChoseCharacterComponent;
  let fixture: ComponentFixture<ModalChoseCharacterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModalChoseCharacterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModalChoseCharacterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

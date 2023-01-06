import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HiphopComponent } from './hiphop.component';

describe('HiphopComponent', () => {
  let component: HiphopComponent;
  let fixture: ComponentFixture<HiphopComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HiphopComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HiphopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
